import React, { Component, createRef, useEffect} from 'react'
import L from 'react-dom-factories'
L_ = React.createElement
import {VictoryChart, VictoryTheme, VictoryLine} from 'victory'



#export default class Vis extends React.Component
export default Vis = (props)->
  {data} = props
  ref = createRef()

  useEffect ()->
    {data} = props
    canvas = ref.current
    ctx = canvas.getContext "2d"
    w = data[0].length
    h = data.length
    console.log('wh',w,h)
    canvas.width =w
    canvas.height = h

    concat = (x,y)->x.concat y

    im = data
      .reduce concat
      .map (v)->v.concat [255]
      .reduce concat

    img = new ImageData(Uint8ClampedArray.from(im),w,h)
    ctx.putImageData img,0,0
    
  L.div className:'image',
    L.canvas ref:ref, style:{width:100,height:100}
