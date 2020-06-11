import React from 'react'
import './style.css'

export default Presenter = ({data, setattr}) =>
  if data is undefined
    return "Loading..."
  on_press = ()->
    console.debug 'down'
    setattr 'depressed', true
  <div className="uicontrols-presenter">
    <button className="button"
      onMouseDown={on_press}
      onMouseUp={()->setattr 'depressed', false}
      >{data.label}</button>
  </div>
