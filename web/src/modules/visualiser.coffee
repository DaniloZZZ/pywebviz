import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement
import Input from './UIcomponents/input.coffee'

export default class Vis extends React.Component
  state:
    value:"None"
  constructor:(props)->
    super props
    step = ()=>
      varname = @state.varname
      props.sendCallback? 'getvar:'+ varname
    setInterval step, 1500
    props.registerCallback @onMessage

  onMessage:(msg)=>
    @setState value:msg
    value = msg

  render:->
    L.div className:'widget',
      L.div 0,"Variable name: ",
      L_ Input,
        default:@state.varname
        onChange:(val)=> @setState varname:val
      @state.value



