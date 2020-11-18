import React from 'react'
import {LibvisModule} from 'libvis'
import './style.less'

PictureWrap = (key, child)->
  <span className='wrap' key={key}>
    {child}
  </span>


export default Presenter = ({data, setattr, addr}) =>
  console.log 'App address: ' + addr
  if data is undefined
    return "Loading..."
  if data.images is undefined
    return "Received handshake..."

  <div className="Gallery-presenter" >
    Gallery of {data.images?.length} images:
      <div className='container'>
      {
        data.images
          .map (x)-> LibvisModule object:x, addr:addr
          #.map (x, i)-> <div>{i} {x}</div>
          .map (x, i)-> PictureWrap i, x
      }
    </div>
  </div>
