import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { 
  LayoutDashboard, 
  Upload, 
  Settings, 
  Calculator, 
  FileText, 
  Cog 
} from 'lucide-react'

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Data Import', href: '/data-import', icon: Upload },
  { name: 'Rule Manager', href: '/rule-manager', icon: Settings },
  { name: 'Payment Calculator', href: '/payment-calculator', icon: Calculator },
  { name: 'Reports', href: '/reports', icon: FileText },
  { name: 'Settings', href: '/settings', icon: Cog },
]

const Sidebar: React.FC = () => {
  const location = useLocation()

  return (
    <div className="w-64 bg-white dark:bg-gray-800 shadow-sm border-r border-gray-200 dark:border-gray-700">
      <div className="flex flex-col h-full">
        <div className="flex items-center justify-center h-16 px-4">
          <h2 className="text-lg font-bold text-gray-900 dark:text-white">
            MFC Payment System
          </h2>
        </div>
        
        <nav className="flex-1 px-4 py-6">
          <ul className="space-y-2">
            {navigation.map((item) => {
              const isActive = location.pathname === item.href
              return (
                <li key={item.name}>
                  <Link
                    to={item.href}
                    className={`flex items-center px-4 py-2 text-sm font-medium rounded-lg transition-colors ${
                      isActive
                        ? 'bg-primary-100 dark:bg-primary-900 text-primary-700 dark:text-primary-300'
                        : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
                    }`}
                  >
                    <item.icon className="mr-3 h-5 w-5" />
                    {item.name}
                  </Link>
                </li>
              )
            })}
          </ul>
        </nav>
      </div>
    </div>
  )
}

export default Sidebar 