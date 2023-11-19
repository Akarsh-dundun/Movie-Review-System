import React from 'react';
import { Tilt } from 'react-tilt';
import { motion } from "framer-motion";

import { banner } from '../assets';
import { textVariant, fadeIn } from '../utils/motion';
import styles from '../styles';
import { topFlicks } from '../constants';

const FlickCard = ( { index, name, poster} ) => {
  return (
      <Tilt className='xs:w-[250px] w-full'>
        <motion.div
          variants={fadeIn("right", "spring", 0.5*index, 0.75)}
          className='w-full green-pink-gradient p-[1px] rounded-[20px] shadow-card'
        >
          <div
            options={{
              max: 45,
              scale: 1,
              speed: 450,
            }}
            className='bg-black rounded-[20px] py-5 px-12 min-h-[280px] flex justify-evenly items-center flex-col'
          >
            <img src={poster} alt={name} className='w-128 h-128 object-contain rounded-[20px]' />
            <h3 className='mt-2 text-white text-[20px] font-bold text-center'>{name}</h3>
          </div>
        </motion.div>
      </Tilt>
  )
}

const Banner = () => {
  return (
    <>
      <motion.div
        variants={textVariant()}
      >
        <h2 className={styles.sectionHeadText}> 
          Latest Movies
        </h2>
      </motion.div>
    
      <div className='w-full mt-3 flex justify-center items-center flex-wrap gap-12'>
        {topFlicks.map((flick, index) => (
          <FlickCard key={flick.name} index={index} {...flick} />
        ))}        
      </div>
    </>
  )
}

export default Banner