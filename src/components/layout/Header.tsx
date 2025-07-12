import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Moon, Sun, Bell, User } from 'lucide-react'
import { toggleDarkMode } from '@store/uiSlice'
import { RootState } from '@store/index'

const Header: React.FC = () => {
  const dispatch = useDispatch()
  const isDarkMode = useSelector((state: RootState) => state.ui.isDarkMode)

  return (
    <header className="w-full bg-white/80 dark:bg-gray-900/80 shadow-lg rounded-b-2xl border-b border-gray-200 dark:border-gray-700 backdrop-blur-md">
      <div className="flex items-center justify-center px-6 py-3 min-h-[56px] gap-1.5">
        <span className="font-bold" style={{ fontFamily: 'Impact, sans-serif', fontSize: 24 }}>Malta Fight Co.</span>
      </div>
    </header>
  )
}

export default Header 