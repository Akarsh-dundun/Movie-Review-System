import React from 'react'
import styles from './styles'
import { Navbar, Banner, Search, Description, Footer } from './components'

const App = () => {
  return (
    <div className='bg- w-full overflow-hidden'>
      <div className={` bg-primary ${styles.paddingX} ${styles.flexCenter}`}>
        <div className={`${styles.boxWidth}`}>
          <Navbar />
        </div>
      </div>

      <div className={`bg-primary ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <Banner />
          <Search />
          <Footer />
        </div>
      </div>
    </div>
  )
}

export default App