import React from 'react'
import { Users, DollarSign, TrendingUp, Calendar } from 'lucide-react'

const Dashboard: React.FC = () => {
  const stats = [
    {
      name: 'Total Attendances',
      value: '287',
      change: '+12%',
      changeType: 'positive',
      icon: Users,
    },
    {
      name: 'Total Revenue',
      value: '€4,256.30',
      change: '+8%',
      changeType: 'positive',
      icon: DollarSign,
    },
    {
      name: 'Group Classes',
      value: '156',
      change: '+5%',
      changeType: 'positive',
      icon: TrendingUp,
    },
    {
      name: 'Private Sessions',
      value: '131',
      change: '+15%',
      changeType: 'positive',
      icon: Calendar,
    },
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Dashboard
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          Welcome to Malta Fight Co. Payment System
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {stats.map((stat) => (
          <div
            key={stat.name}
            className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6"
          >
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <stat.icon className="h-8 w-8 text-primary-600 dark:text-primary-400" />
              </div>
              <div className="ml-4 flex-1">
                <p className="text-sm font-medium text-gray-600 dark:text-gray-400">
                  {stat.name}
                </p>
                <p className="text-2xl font-bold text-gray-900 dark:text-white">
                  {stat.value}
                </p>
              </div>
            </div>
            <div className="mt-4">
              <span className="text-sm text-green-600 dark:text-green-400">
                {stat.change}
              </span>
              <span className="text-sm text-gray-600 dark:text-gray-400 ml-1">
                from last month
              </span>
            </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
            Quick Actions
          </h3>
          <div className="space-y-3">
            <button className="w-full btn-primary">
              Import Monthly Data
            </button>
            <button className="w-full btn-secondary">
              Calculate Payments
            </button>
            <button className="w-full btn-secondary">
              Generate Reports
            </button>
          </div>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">
            Recent Activity
          </h3>
          <div className="space-y-3">
            <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
              <span className="w-2 h-2 bg-green-500 rounded-full mr-3"></span>
              May attendance data imported (608 records)
            </div>
            <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
              <span className="w-2 h-2 bg-blue-500 rounded-full mr-3"></span>
              Payment rules updated for "Adult 10 Pack"
            </div>
            <div className="flex items-center text-sm text-gray-600 dark:text-gray-400">
              <span className="w-2 h-2 bg-purple-500 rounded-full mr-3"></span>
              Historical payment data refreshed (667 records)
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard 