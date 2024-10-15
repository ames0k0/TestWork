import React from 'react';


function MozillaCommunity(props) {
  return (
    <ul>
      <li>technologists</li>
    </ul>
  );
}

function MetaInfo(props) {
  return (
    <div className="MozillaMeta">
      <h1>At Mozilla, we're a global community of</h1>
      <MozillaCommunity />
      <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
    </div>
  )
}

function PikaDescription(props) {
  return <p className="editor-note">My cat is very <strong>very grumpy</strong></p>
}


function PikaPika(props) {
  return (
    <div className="myPika">
      <PikaDescription />
      <img
        onClick={props.handleClick}
        style={{width: props.width, height: props.height}}
        src="https://i.pinimg.com/originals/26/76/3d/26763d481172f5dc599d151570b38ded.png" alt="" />
    </div>
  )
}


class PikaU extends React.Component {
  constructor(props) {
    super(props);
    this.state = {width: "100px", height: "100px"};
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(e) {
    this.setState(
      {
        width: (this.state.width === "100px") ? "200px" : "100px",
        height: (this.state.height === "100px") ? "200px" : "100px",
      }
    );
  }

  render() {
    return (
      <div className="container">
        <MetaInfo />
        <PikaPika width={this.state.width} height={this.state.height} handleClick={this.handleClick} />
      </div>
    );
  }
}

export default PikaU;
