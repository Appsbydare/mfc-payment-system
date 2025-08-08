import sqlite3 from 'sqlite3';

// Database path
const dbPath = './database.sqlite';

export const db = new sqlite3.Database(dbPath);

// Enable foreign keys
db.run('PRAGMA foreign_keys = ON');

// Create tables if they don't exist
export const initializeDatabase = () => {
  // Users table
  db.run(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL,
      role TEXT DEFAULT 'user',
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Attendance table
  db.run(`
    CREATE TABLE IF NOT EXISTS attendance (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      customer_name TEXT NOT NULL,
      package_name TEXT NOT NULL,
      session_type TEXT NOT NULL,
      coach_name TEXT,
      attendance_date DATE NOT NULL,
      session_count INTEGER DEFAULT 1,
      total_sessions INTEGER,
      package_price DECIMAL(10,2),
      discount_amount DECIMAL(10,2) DEFAULT 0,
      discount_reason TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Payment rules table
  db.run(`
    CREATE TABLE IF NOT EXISTS payment_rules (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      rule_name TEXT UNIQUE NOT NULL,
      session_type TEXT NOT NULL,
      coach_percentage DECIMAL(5,2) NOT NULL,
      bgm_percentage DECIMAL(5,2) NOT NULL,
      management_percentage DECIMAL(5,2) NOT NULL,
      mfc_percentage DECIMAL(5,2) NOT NULL,
      is_fixed_rate BOOLEAN DEFAULT 0,
      fixed_amount DECIMAL(10,2),
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Coaches table
  db.run(`
    CREATE TABLE IF NOT EXISTS coaches (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      email TEXT,
      phone TEXT,
      is_active BOOLEAN DEFAULT 1,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Reports table
  db.run(`
    CREATE TABLE IF NOT EXISTS reports (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      report_type TEXT NOT NULL,
      report_data TEXT NOT NULL,
      generated_by INTEGER,
      generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (generated_by) REFERENCES users(id)
    )
  `);

  // Insert default payment rules
  const defaultRules = [
    {
      rule_name: 'Group Classes Default',
      session_type: 'group',
      coach_percentage: 43.5,
      bgm_percentage: 30.0,
      management_percentage: 8.5,
      mfc_percentage: 18.0,
      is_fixed_rate: 0
    },
    {
      rule_name: 'Private Sessions Default',
      session_type: 'private',
      coach_percentage: 80.0,
      bgm_percentage: 15.0,
      management_percentage: 0.0,
      mfc_percentage: 5.0,
      is_fixed_rate: 0
    }
  ];

  const insertRule = db.prepare(`
    INSERT OR IGNORE INTO payment_rules 
    (rule_name, session_type, coach_percentage, bgm_percentage, management_percentage, mfc_percentage, is_fixed_rate)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `);

  defaultRules.forEach(rule => {
    insertRule.run(
      rule.rule_name,
      rule.session_type,
      rule.coach_percentage,
      rule.bgm_percentage,
      rule.management_percentage,
      rule.mfc_percentage,
      rule.is_fixed_rate
    );
  });

  console.log('✅ Database initialized successfully');
};

export default db; 