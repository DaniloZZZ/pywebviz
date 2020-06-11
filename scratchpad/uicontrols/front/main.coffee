import React from 'react'
import './style.css'

button = ({data, setattr}) =>
  on_press = ()->
    console.debug 'down'
    setattr 'depressed', true
  <div className="uicontrols-presenter">
    <button className="button"
      onMouseDown={on_press}
      onMouseUp={()->setattr 'depressed', false}
      >{data.label}</button>
  </div>


slider = ({data, setattr}) =>
  <div className="uicontrols-presenter">
    <div className="slider-group">
      <input type='range' className="slider"
        min={data.min}
        max={data.max}
        value={data.value}
        onChange={(e)->setattr 'value', e.target.value}
        />
      <label>{data.value}</label>
    </div>
  </div>

modules =
  button: button
  slider: slider

export default Presenter = ({data, setattr}) =>
  if data is undefined
    return "Loading.."
  if data.type is undefined
    return "Loading..."
  f = modules[data.type]
  try
    return f({data, setattr})
  catch
    return JSON.stringify data

