import React from 'react'
import './style.css'

export default PNGPresenter= ({data, setattr}) =>
  console.log('image data', data)
  if data is undefined
    return "Loading..."
  <div className="Image-presenter">
    <img src={"data:image/png;base64," + data.image} />
  </div>
