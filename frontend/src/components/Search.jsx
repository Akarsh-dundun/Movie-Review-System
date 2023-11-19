import React from 'react'
import { useState } from 'react'
import axios from 'axios';
import APIService from './APIServices';
import Description from './Description';


const Search = () => {

  const [content, setContent] = useState('')
  const [response, setResponce] = useState('')

  const insertArticle = () =>{
    APIService.InsertArticle({content})
    .then((response) => {setResponce(response)})
    .catch(error => console.log('error',error))
  }

  const handleSubmit=(event)=>{ 
    event.preventDefault()
    insertArticle()
    setContent('')
  }

  return (
    <>
      <div className='w-full flex items-center justify-center py-12'>
        <form onSubmit={handleSubmit}>   
          <div>
              <label
              htmlFor='content' 
              className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                Enter Movie Name
              </label>
              <input 
                type="text" 
                id="movie_name" 
                value={content}
                onChange={e => setContent(e.target.value)}
                className="bg-gray-50 w-[500px] border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Movie Name" required 
              />
          </div>
          <div className='py-4 flex items-center justify-center'>
            <button 
              type="submit" 
              className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Submit
            </button>
          </div>    

        </form>
      </div>
      {response === '' ? <p>nothing in here</p> : <Description verdict={response} />}
    </>
  )
}

export default Search