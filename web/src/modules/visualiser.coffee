import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement
import Input from './UIcomponents/input.coffee'
import LineGraph from './presenters/lineGraph_recharts.coffee'
import MplD3 from './presenters/mpld3.coffee'
import Image from './presenters/image.coffee'

export default class Vis extends React.Component
  state:
    value:"None"
  constructor:(props)->
    super props

  choosePresenter: (val)->
    if @props.type=='mpl'
      return MplD3
    if @props.type=='img'
      return Image
    if val is null
      return ({data})->L.div 0,data
    try
      if val.length>10
        if val[0].length>10
          console.log 'image'
          return Image
    catch
      print("error", val)
    switch typeof val
      when 'object' then LineGraph
      else ({data})->L.div 0,data

  render:->
    Pres = @choosePresenter @props.value
    L.div className:'widget',
      L.div className:'title',"Name: ",
      L_ Input,
        default:@props.varname
        onChange:@props.onNameChange
      L_ Pres, data:@props.value
      #@props.value



