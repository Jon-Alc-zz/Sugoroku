class BoardDisplay extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		console.log(this.props.getJSONFile);
		return(
			<div>
				{this.props.getSpaceKeys}
			</div>
		);
	}
}