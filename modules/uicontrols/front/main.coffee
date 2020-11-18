import React from 'react'
import './style.css'

button = ({data, setattr}) =>
  on_press = ()->
    console.debug 'down'
    setattr 'depressed', true
  <div className="uicontrols-presenter">
    <button className="button nodrag"
      onMouseDown={on_press}
      onMouseUp={()->setattr 'depressed', false}
      >{data.label}</button>
  </div>


slider = ({data, setattr}) =>
  round = (value) =>
    v = Number.parseFloat(value.toPrecision(6))
    console.log 'rounded', v, value
    return v
  wheelstep = round(0.02 * (data.max-data.min))
  console.log 'wheelstep', wheelstep
  <div className="uicontrols-presenter">
    <div className="slider-group">
      <input type='range' className="slider"
        min={data.min}
        max={data.max}
        value={data.value}
        onChange={(e)->setattr 'value', e.target.value}
        step={round(wheelstep/2)}
        onWheel={(e)->
          console.log 'wheel ev', e.deltaY
          setattr 'value', round( -Math.sign(e.deltaY)*wheelstep + Number(data.value))
        }
        />
      <label>{data.value}</label>
    </div>
  </div>

modules =
  button: button
  slider: slider

export default Presenter = ({data, setattr}) =>
  console.log 'Data in uicontrols', data
  if data is undefined
    return "Loading.."
  if data.type is undefined
    return "Loading..."
  f = modules[data.type]
  return f({data, setattr})

