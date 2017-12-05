class JSONParser extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			title: "",
			author: "",
			dice: "",
			numSpaces: 0,
			spaceKeys: []
		};

		this.parser = this.parser.bind(this);
	}

	parser(){
		var xmlHttp = new XMLHttpRequest();

    	xmlHttp.onreadystatechange = function() { 
        	if (xmlHttp.readyState == 4){
        		var XMLResponse = JSON.parse(xmlHttp.responseText);
        		if(xmlHttp.status == 200){
        			console.log(XMLResponse);
        			this.setState({
        				title: XMLResponse.title,
        				author: XMLResponse.author,
        				dice: XMLResponse.dice,
        				numSpaces: Object.keys(XMLResponse.transitions).length
        			},()=>{
        				var tempKeys = []
        				for(var k in XMLResponse.transitions){
        					tempKeys.push(k);
        				}

        				this.setState({
        					spaceKeys: tempKeys
        				}, ()=>{
        					console.log(this.state.title);
        					console.log("Created by " + this.state.author);
        					console.log("Use " + this.state.dice + " to play");

        					console.log(this.state.spaceKeys);
        				});
        			});

        		}else{
        			console.log("Can't parse");
        		}
        	}
        }.bind(this);

        xmlHttp.open("GET", "data/JonTestFile.json", true);
        xmlHttp.send(null);
	}

	render(){
		return(
			<div>
				<button onClick={this.parser}>Click Ryan</button>
			</div>
		);
	}
}