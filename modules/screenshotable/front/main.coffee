import React, { useRef, useEffect } from 'react'
import {LibvisModule} from 'libvis'
import './style.css'
import html2canvas from 'html2canvas'

get_screenshot = (element)=>
  html2canvas(element).then (canvas)=>
    img = canvas.toDataURL 'image/png'
    return img
open_in_new_tab = (element)=>
  get_screenshot element
    .then (image) =>
      w = window.open('', '_blank')
      w.document.write('<img id="image" src="'+image+'"/>')
      w.document.close()

export default Presenter = ({data, setattr, addr}) =>
  wrapEl = useRef null
  if data is undefined
    return "Loading..."
  if data.get_image
    get_screenshot wrapEl.current
      .then (image) => setattr 'image', image
  <div className="screenshotable-presenter" >
    <div className='wrapper' ref={wrapEl}>
      <LibvisModule object={data.object} addr={addr} />
    </div>
    <div className='horisontal-flex'>
      <button
        onClick={()=>open_in_new_tab wrapEl.current}>
        Open image in new tab
      </button>
      <button
        onClick={()=>setattr 'trigger', true}>
        Send image to python object
      </button>
    </div>

  </div>
