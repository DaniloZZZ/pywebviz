import React from 'react'
import './style.css'

export default Presenter = ({data, setattr}) =>
  console.log "got data", data

  if data is undefined
    return "Loading..."

  if data.value is undefined
    return "Waiting..."

  <div className="func-presenter">
    Some data.value: `<p>{'ht'+data.value}</p>`
  </div>
