import { googleSheetsService } from '../services/googleSheets';

// Initialize database function
export const initializeDatabase = async () => {
  try {
    // Check if Google Sheets is accessible
    const isHealthy = await googleSheetsService.healthCheck();
    
    if (!isHealthy) {
      throw new Error('Google Sheets service is not accessible');
    }

    // Initialize database with default structure
    await googleSheetsService.initializeDatabase();
    
    console.log('✅ Google Sheets database initialized successfully');
    console.log(`🌍 Environment: ${process.env.NODE_ENV || 'development'}`);
  } catch (error) {
    console.error('❌ Failed to initialize Google Sheets database:', error);
    throw error;
  }
};

export { googleSheetsService as db }; 