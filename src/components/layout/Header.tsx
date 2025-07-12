import React from 'react'

const Header: React.FC = () => {
  return (
    <header className="w-full bg-white/30 dark:bg-gray-900/30 shadow-lg border-b border-gray-200 dark:border-gray-700 backdrop-blur-md">
      <div className="flex items-center justify-center px-6 py-3 min-h-[56px] gap-1.5">
        <span style={{ fontFamily: 'Impact, sans-serif', fontSize: 42 }}>Malta Fight Co. - Payment Automation System </span>
      </div>
    </header>
  )
}

export default Header 