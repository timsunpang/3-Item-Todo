import React from 'react';
import DateFilter from './DateFilter'
import TodoList from './TodoList'

class Main extends React.Component {
	constructor(props) {
		super(props);
		this.renderTodos = this.renderTodos;
	}


	componentDidMount() {
		this.props.getTodos();
	}

	render() { 
		return (
			<div>
				3 Item Todo
				<DateFilter/>
				<TodoList {...this.props}/>
			</div>
		)
	}
}


export default Main