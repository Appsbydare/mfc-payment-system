# Malta Fight Co. - Payment Automation System

A modern web-based payment automation system for Malta Fight Co.'s combat sports gym, built with React, TypeScript, and Tailwind CSS.

## 🚀 Features

- **Dashboard**: Real-time metrics and quick actions
- **Data Import**: CSV file upload and processing
- **Rule Manager**: Payment rules and membership configuration
- **Payment Calculator**: Automated payment calculations
- **Reports**: Generate and export payment reports
- **Settings**: System configuration and user preferences

## 🛠 Tech Stack

- **Frontend**: React 18 + TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Redux Toolkit
- **Routing**: React Router
- **Data Fetching**: React Query
- **Forms**: React Hook Form
- **Icons**: Lucide React
- **Build Tool**: Vite

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/mfc-payment-system.git
cd mfc-payment-system
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🏗 Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── layout/         # Layout components
│   ├── dashboard/      # Dashboard components
│   ├── data-import/    # Data import components
│   ├── rule-manager/   # Rule management components
│   ├── payment-calculator/ # Payment calculator components
│   ├── reports/        # Report components
│   ├── settings/       # Settings components
│   ├── common/         # Common UI components
│   └── ui/            # UI utilities
├── pages/             # Page components
├── hooks/             # Custom React hooks
├── services/          # API services and utilities
├── store/             # Redux store and slices
├── styles/            # Global styles
└── constants/         # Application constants
```

## 🔧 Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run test` - Run tests
- `npm run e2e` - Run end-to-end tests

### Environment Variables

Create a `.env.local` file in the root directory:

```env
VITE_API_URL=http://localhost:5000/api
VITE_APP_NAME=Malta Fight Co. Payment System
```

## 🚀 Deployment

### Vercel Deployment

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy to Vercel:
```bash
vercel
```

### Manual Deployment

1. Build the project:
```bash
npm run build
```

2. Deploy the `dist` folder to your hosting provider.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support, email support@maltafightco.com or create an issue in this repository. 