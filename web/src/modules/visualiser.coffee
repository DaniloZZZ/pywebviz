import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement
import Input from './UIcomponents/input.coffee'
import LineGraph from './presenters/lineGraph_recharts.coffee'
import MplD3 from './presenters/mpld3.coffee'
import Image from './presenters/image.coffee'
import * as Modules from './presenters'
import {installed} from './presenters'
Object.assign( Modules, installed )
console.log(Modules)

get_var_type = (type, val)->
  if type=='mpl'
    return 'MplD3'
  if type=='img'
    return 'Image'
  if val is null
    return 'Raw'
  try
    if val.length>10
      if val[0].length>10
        return 'Image'
  catch
  if Array.isArray(val)
    return 'LineGraph'
  if type=='raw'
    return 'Raw'
    
  return type

export choosePresenter = (type, val)->
  console.log "Choosing presenter for '#{type}' value:", val, "from", Modules
  type = get_var_type type, val
  presenter = Modules[type]
  if presenter
    return presenter
  else
    return ({data})->L.div 0,JSON.stringify data

export default Vis = (props)->
  {variable, name, onNameChange} = props
  Pres = choosePresenter variable.type, variable.value
  L.div className:'vis',
    L.div className:'title',"Name: ",
    L_ Input,
      value:name
      onChange:onNameChange
    L_ Pres, data:variable.value, addr:props.addr
