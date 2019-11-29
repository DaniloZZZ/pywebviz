import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement
import Input from './UIcomponents/input.coffee'
import LineGraph from './presenters/lineGraph_recharts.coffee'
import MplD3 from './presenters/mpld3.coffee'
import Image from './presenters/image.coffee'

choosePresenter = (type, val)->
  if type=='mpl'
    return MplD3
  if type=='img'
    return Image
  if val is null
    return ({data})->L.div 0,data
  try
    if val.length>10
      if val[0].length>10
        return Image
  catch
  switch typeof val
    when 'object' then LineGraph
    else ({data})->L.div 0,data

export default Vis = (props)->
  {variable, onNameChange} = props
  Pres = choosePresenter variable.type, variable.value
  L.div className:'vis',
    L.div className:'title',"Name: ",
    L_ Input,
      value:variable.name
      onChange:onNameChange
    L_ Pres, data:variable.value



