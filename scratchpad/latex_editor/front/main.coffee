import React from 'react'
import {MathFieldComponent} from 'react-mathlive'
import './style.css'

export default Presenter = ({data, setattr}) =>
  if data is undefined
    return "Loading..."
  console.log data
  <div className="latex-presenter">
    <div>
      MathField:
      <MathFieldComponent latex={data.tex} />
      <br/>
      TextField:
    </div>
  </div>
