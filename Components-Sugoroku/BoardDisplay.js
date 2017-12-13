class BoardDisplay extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		console.log(this.props.getJSONFile);
		var spaceKeyArr = this.props.getSpaceKeys;
		var boardDisplayArr = [];
		var rule = "";

		for(var i = 0; i < spaceKeyArr.length; i++){
			console.log(this.props.getJSONFile["transitions"][spaceKeyArr[i]]);
			var isStart = false;
			var isEnd = false;
			var isJump = false;

			if(this.props.getJSONFile["transitions"][spaceKeyArr[i]]["rule"] != null){
				rule = this.props.getJSONFile["transitions"][spaceKeyArr[i]]["rule"];
			}

			if(i == 0){
				isStart = true;
			}

			if(i == spaceKeyArr.length-1){
				isEnd = true;
			}

			boardDisplayArr.push(<BoardSpace
									key={i}
									spaceID={spaceKeyArr[i]}
									isStart={isStart}
									isEnd={isEnd}
									isJump={isJump}
									rule={rule} />);
		}

		return(
			<div>
				{boardDisplayArr}
			</div>
		);
	}
}