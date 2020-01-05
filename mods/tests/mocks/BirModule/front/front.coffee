import React from 'react'
import './style.css'

export default Vis = ({data, setattr}) =>
  data = data.split('\n')
  return ( <div className="beer">
    <h2>Beer song!</h2>
    <div className='input'>
     <input type='text' onChange={(e)=>setattr 'count', e.target.value}></input>
    </div>
    {data.map (s)->
      <p>{s}</p>
    }
  </div>
  )

