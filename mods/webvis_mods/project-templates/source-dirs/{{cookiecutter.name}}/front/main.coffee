import React from 'react'
import './style.css'

export default Presenter = ({data, setattr}) =>
  <div className="{{cookiecutter.name}}-presenter">
    Random quote: `<p>{data.quote}</p>`
  </div>
