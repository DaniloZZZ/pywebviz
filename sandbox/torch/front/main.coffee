import React from 'react'
import './style.less'

export default Presenter = ({data, setattr}) =>
  {tensor} = data

  if tensor is undefined
    return 'Wait...'

  len = tensor.length

  get_style=(val)=>
    return
      backgroundColor:"hsl(0,10%,#{20+val*80}%)"
      fontSize: "#{250/len}px"
      padding: "#{20//len}px"
      margin: "#{20//len}px"
  <div className="torch-presenter">
    Torch tensor:
    <table>
      <tbody>
        {
            tensor.map (row, i)=>
              if Array.isArray row
                <tr key={i}>
                {
                  row.map (val, j) =>
                    <td style={get_style val} key={j}>{val.toFixed(3)}</td>
                }
                </tr>
              else
                <tr key={i}>{row}</tr>
        }
      </tbody>
    </table>
  </div>
