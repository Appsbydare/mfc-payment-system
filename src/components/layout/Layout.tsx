import React from 'react'
import Header from './Header'
import Sidebar from './Sidebar'

interface LayoutProps {
  children: React.ReactNode
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-100 dark:bg-gray-900">
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header />
        <main className="flex-1 overflow-x-hidden overflow-y-auto bg-transparent flex justify-center items-start">
          <div className="w-full max-w-5xl mx-auto mt-6 mb-6 px-4 py-6 bg-white/90 dark:bg-gray-800/90 rounded-2xl shadow-xl border border-gray-200 dark:border-gray-700">
            {children}
          </div>
        </main>
      </div>
    </div>
  )
}

export default Layout 