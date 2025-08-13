import low from 'lowdb';
import FileSync from 'lowdb/adapters/FileSync';
import path from 'path';

// Database file path - use /tmp for Vercel serverless
const dbPath = process.env.NODE_ENV === 'production' 
  ? '/tmp/data.json' 
  : path.join(__dirname, '../../data.json');

// Create adapter and database instance
const adapter = new FileSync(dbPath);
const db = low(adapter);

// Set default data structure
db.defaults({
  users: [],
  attendance: [],
  payment_rules: [
    {
      id: 1,
      rule_name: 'Group Classes Default',
      session_type: 'group',
      coach_percentage: 43.5,
      bgm_percentage: 30.0,
      management_percentage: 8.5,
      mfc_percentage: 18.0,
      is_fixed_rate: false,
      created_at: new Date().toISOString()
    },
    {
      id: 2,
      rule_name: 'Private Sessions Default',
      session_type: 'private',
      coach_percentage: 80.0,
      bgm_percentage: 15.0,
      management_percentage: 0.0,
      mfc_percentage: 5.0,
      is_fixed_rate: false,
      created_at: new Date().toISOString()
    }
  ],
  coaches: [],
  reports: []
}).write();

// Initialize database function
export const initializeDatabase = () => {
  console.log('✅ Database initialized successfully with lowdb');
  console.log(`📁 Database file: ${dbPath}`);
  console.log(`🌍 Environment: ${process.env.NODE_ENV || 'development'}`);
};

export default db; 