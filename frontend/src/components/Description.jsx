import React from 'react'
import { Tilt } from 'react-tilt'
import { motion } from 'framer-motion'
import { useState } from 'react'

import { fadeIn, textVariant } from '../utils/motion'
import styles from '../styles'
import { AiFillStar } from "react-icons/ai";

const Description = ( {verdict} ) => {

  console.log(verdict)

  return (
    <>
      <div className='w-full flex items-center justify-center'>
        <Tilt classname="w-full">
          <motion.div
          variants={fadeIn("right","spring",0.5, 0.75)}
            className='w-full green-pink-gradient p-[1px] rounded-[20px] shadow-card'
          >
           <div 
            options = {{
              max: 30,
              scale: 1,
              speed: 200
            }}
            className='bg-black rounded-[20px] py-5 px-12 min-h-[280px] flex justify-evenly items-center flex-col'
          >
            <div className={`${styles.flexStart} md:flex-row flex-col mb-8 w-full`}>
              <div className='flex-1 flex flex-col justify-start mr-10'>
                  <img 
                    src={verdict['poster']} 
                    alt='poster_url'
                    className='w-56 h-96 object contain rounded-[20px]'
                  />
                <h4 className={`${styles.heroHeadText}`}>
                  <a href={verdict['url']}
                  className='hover:text-secondary'
                  >
                    {verdict['movie_name']}
                  </a>
                </h4>
                <p className={`${styles.paragraph} max-w-[500px]`}>
                  {verdict['description']}
                </p>
                <br />
                <p className={`${styles.paragraph}`}>
                  Director: {verdict['director_name']}
                </p>
                <p className={`${styles.paragraph}`}>
                  Actors: {verdict['Actors'][0]}, {verdict['Actors'][1]}, {verdict['Actors'][2]}
                </p>
              </div>
            </div>
            <p className={`font-poppins font-bold text-white text-[28px] leading-[30.8px] py-4 flex align-items`}>
              ImDb Rating: <AiFillStar className='mr-1.5 ml-1.5'/> {verdict['stars']} / 10
            </p>
            <p className={`font-poppins font-bold text-white text-[34px] leading-[30.8px] py-4`}>
              Final Verdict: {verdict['result']}
            </p>
          </div> 
          </motion.div>
        </Tilt>
      </div> 
    </>
  )
}

export default Description;