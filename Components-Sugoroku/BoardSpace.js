class BoardSpace extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		var pic = <img src="../data/space.png" width="50px" height="50px" className="spaceImg"></img>

		if(this.props.isEnd || this.props.isStart){
			pic = <img src="../data/checkpoint.png" width="50px" height="50px" className="spaceImg"></img>
		}
		return(
			<div className="space">
				{pic}
				<span className="spaceID">{this.props.spaceID}</span>
				<img src="../data/rightArrow.png" width="40px" height="40px" className="spaceImg" 
					style={{display: this.props.isEnd ? "none":"inline-block"}}></img>
			</div>
		);
	}
}