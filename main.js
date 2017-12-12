var {Router,
	Route,
	IndexRoute,
	IndexLink,
	hashHistory,
	Link} = ReactRouter;

class Main extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div>
				<Navbar />
				{this.props.children}
			</div>
		);
	}
}

ReactDOM.render(
	<Router history={ReactRouter.hashHistory}>
		<Route path="/" component={Main}>
			<IndexRoute component={SugorokuHome}/>
			<Route path="history" component={SugorokuHistory}/>
			<Route path="algorithm" component={SugorokuAlgorithm}/>
			<Route path="about" component={AboutUs}/>
		</Route>
	</Router>,
	document.getElementById("container")
);