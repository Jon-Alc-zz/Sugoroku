class Navbar extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div id="navbar">
				<IndexLink to="/" className="routerLink" activeClassName="active">Home</IndexLink>
				<Link to="history" className="routerLink" activeClassName="active">History</Link>
				<Link to="about" className="routerLink" activeClassName="active">About Us</Link>
			</div>
		);
	}
}