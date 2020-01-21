import React from 'react'
import './style.css'
import { VueInReact } from 'vuera'
import Field from './fieldplay/src/App.vue'
import main from './fieldplay/src/lib/nativeMain.js'

scene = undefined
export default Presenter = ({data, setattr}) =>
  console.log 'foobar'
  {code, options} = data
  console.log "code: ", code
  console.log "options: ", options
  if scene is undefined
    scene = main()
  if code is undefined
    code ="
vec2 get_velocity(vec2 p) {\n
  return p;\n
}"
  <div className="vector_field-presenter">
      <canvas id="scene"
      style={{width: "100%", height: "100%"}}
      width = "300" height = "400"
      />
    <Field options={options} scene={scene} code={code}/>
  </div>
