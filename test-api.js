// Test script for MFC Payment System API
const API_BASE = 'https://mfc-payment-system.vercel.app';

async function testEndpoint(endpoint, method = 'GET', body = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    if (body) {
      options.body = JSON.stringify(body);
    }

    console.log(`Testing ${method} ${endpoint}...`);
    const response = await fetch(`${API_BASE}${endpoint}`, options);
    
    console.log(`Status: ${response.status} ${response.statusText}`);
    
    if (response.ok) {
      const data = await response.json();
      console.log('Response:', JSON.stringify(data, null, 2));
    } else {
      const errorText = await response.text();
      console.log('Error Response:', errorText);
    }
    
    console.log('---');
  } catch (error) {
    console.error(`Error testing ${endpoint}:`, error.message);
    console.log('---');
  }
}

async function runTests() {
  console.log('🧪 Testing MFC Payment System API\n');
  
  // Test health endpoint
  await testEndpoint('/api/health');
  
  // Test payment rules endpoint
  await testEndpoint('/api/payments/rules');
  
  // Test global settings endpoint
  await testEndpoint('/api/payments/settings');
  
  // Test data import endpoint
  await testEndpoint('/api/data/import');
  
  console.log('✅ API testing completed');
}

// Run tests if this script is executed directly
if (typeof window === 'undefined') {
  runTests();
} else {
  // Browser environment
  window.testAPI = runTests;
  console.log('API test function available as window.testAPI()');
} 