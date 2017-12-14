class JSONParser extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			title: "",
			author: "",
			dice: "",
			numSpaces: 0,
			spaceKeys: [],
            currentBoard:"--"
		};

		this.parser = this.parser.bind(this);
        this.showList = this.showList.bind(this);
        this.changeName = this.changeName.bind(this);
	}

    changeName(e, name, url){
        e.preventDefault();
        //e.stopPropagation();
        this.setState({
            currentBoard: name
        },()=>{
            this.parser(url);
        });
    }

	parser(url){
		var xmlHttp = new XMLHttpRequest();

    	xmlHttp.onreadystatechange = function(e) { 
        	if (xmlHttp.readyState == 4){
        		var XMLResponse = JSON.parse(xmlHttp.responseText);
        		if(xmlHttp.status == 200){
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
        					this.props.setJSONFile(XMLResponse);
        					this.props.setSpaceKeys(this.state.spaceKeys);
        				});
        			});

        		}else{
        			console.log("Can't parse");
        		}
        	}
        }.bind(this);

        xmlHttp.open("GET", url, true);
        xmlHttp.send(null);
	}

    showList(){
        document.getElementById("dropdownList").classList.toggle("show");
    }

	render(){
		return(
			<div id="sugorokuBoardButton">
                <div id="currentDropdown" onClick={this.showList}>
                    {this.state.currentBoard}

                    <i className="glyphicon glyphicon-menu-down dropdownIcon"></i>
                </div>

                <div id="dropdownList" className="dropdownContent">
                    <a href="#">--</a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 1", "Python-Sugoroku/Python-Sugoroku/input_board.json")}>
                        Board 1
                    </a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 2", "Python-Sugoroku/Python-Sugoroku/ExampleBoards/board1.json")}>
                        Board 2
                    </a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 3", "Python-Sugoroku/Python-Sugoroku/ExampleBoards/board2.json")}>
                        Board 3
                    </a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 4", "Python-Sugoroku/Python-Sugoroku/ExampleBoards/board3.json")}>
                        Board 4
                    </a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 5", "Python-Sugoroku/Python-Sugoroku/ExampleBoards/board4.json")}>
                        Board 5
                    </a>

                    <a href="#" onClick={(e)=>this.changeName(e,"Board 6", "Python-Sugoroku/Python-Sugoroku/ExampleBoards/board5.json")}>
                        Board 6
                    </a>
                </div>
			</div>
		);
	}
}

window.onclick = function(event) {
    if (!event.target.matches('#currentDropdown')) {
        var dropdowns = document.getElementsByClassName("dropdownContent");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}