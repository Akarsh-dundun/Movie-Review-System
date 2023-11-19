import React from 'react'
import { useState } from 'react'

import { logo, logo2, logo3 } from '../assets'

const Navbar = () => {
  return (
    <nav className='w-full flex py-6 justify-between items-center navbar'>
      <img 
        src={logo3}
        alt='RatetheReels'
        className='w-[180px] h-[120px]'
      />
    </nav>
  )
}

export default Navbar