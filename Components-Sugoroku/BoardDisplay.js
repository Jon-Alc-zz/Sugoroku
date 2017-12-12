class BoardDisplay extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		console.log(this.props.getJSONFile);
		var spaceKeyArr = this.props.getSpaceKeys;
		var boardDisplayArr = [];

		for(var i = 0; i < spaceKeyArr.length; i++){
			var isStart = false;
			var isEnd = false;
			var isJump = false;

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
									isJump={isJump} />);
		}

		return(
			<div>
				{boardDisplayArr}
			</div>
		);
	}
}