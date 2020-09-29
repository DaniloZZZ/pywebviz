import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import useLegimens from 'legimens'

export wrapModuleWithLegimens = (Pres) => ({data, addr}) =>
  {data, status, respond} = useLegimens {addr, ref:data}
  data
  variable=data
  setattr=respond
  console.log "in wrapper of #{Pres} variable #{variable}"
  console.log 'wrapping pres', Pres
  if variable is undefined
    variable = value:'Loading', type:'raw'
    content = "Loading"
  else
    try
      variable = JSON.parse variable
    catch
      content = "data error"

  L.div className:'contents',
    L_ Pres, data:variable, addr:addr, setattr:setattr

