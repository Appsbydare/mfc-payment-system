import { Router } from 'express';

const router = Router();

// @desc    Calculate payments
// @route   POST /api/payments/calculate
// @access  Private
router.post('/calculate', (req, res) => {
  res.json({ message: 'Calculate payments - TODO' });
});

// @desc    Get payment rules
// @route   GET /api/payments/rules
// @access  Private
router.get('/rules', (req, res) => {
  res.json({ message: 'Get payment rules - TODO' });
});

// @desc    Update payment rules
// @route   PUT /api/payments/rules
// @access  Private
router.put('/rules', (req, res) => {
  res.json({ message: 'Update payment rules - TODO' });
});

// @desc    Get coach payments
// @route   GET /api/payments/coaches
// @access  Private
router.get('/coaches', (req, res) => {
  res.json({ message: 'Get coach payments - TODO' });
});

// @desc    Get BGM payments
// @route   GET /api/payments/bgm
// @access  Private
router.get('/bgm', (req, res) => {
  res.json({ message: 'Get BGM payments - TODO' });
});

export default router; 