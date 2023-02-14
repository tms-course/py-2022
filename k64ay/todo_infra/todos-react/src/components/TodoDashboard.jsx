import React, { Suspense } from 'react';

import Header from '../components/Header';
import InputTodo from '../components/InputTodo';
import TodoItem from '../components/TodoItem';
import { useTodoContext } from '../providers/todo.provider';


const TodoDashboard = () => {
    const {
        results, has_next, has_prev, showComplete,
        addTodo, updateTodo, deleteTodo,
        nextPage, prevPage, toggleShowComplete, switchOrder,
    } = useTodoContext();

    function loadNext() {
        has_next && nextPage();
    }

    function loadPrev() {
        has_prev && prevPage();
    }

    function onChangeOrder(e) {
        console.log(e.target.value);
        switchOrder(e.target.value);
    }

    return (
        <div className="todo-dashboard">
            <Header />
            <InputTodo addTodo={addTodo} />
            <div className="row">
                <div className="col-4 form-check form-switch">
                    <input
                        className="form-check-input"
                        type="checkbox"
                        role="switch"
                        id="completed"
                        value={showComplete}
                        onChange={toggleShowComplete}
                    />
                    <label className="form-check-label" htmlFor="completed">
                        Show Complete
                    </label>
                </div>
                <div className="col-sm-5"></div>
                <div className="col-3">
                    <select 
                        className="form-select form-select-sm" 
                        aria-label=".form-select-sm example"
                        onChange={onChangeOrder}
                    >
                        <option value="-created_at">new first</option>
                        <option value="created_at">old first</option>
                    </select>
                </div>
            </div>
            <Suspense fallback={<h2>Fetching ...</h2>}>
                <ul>
                    {results.map((todo) => (
                        <TodoItem
                            key={todo.id}
                            todo={todo}
                            deleteTodo={deleteTodo}
                            updateTodo={updateTodo}
                        />
                    ))}
                </ul>
                <nav aria-label="Page navigation example">
                    <ul className="pagination justify-content-center">
                        <li className={`page-item ${has_prev || 'disabled'}`} onClick={loadPrev}>
                            <a className="page-link">Prev</a>
                        </li>
                        <li className={`page-item ${has_next || 'disabled'}`} onClick={loadNext}>
                            <a className="page-link">Next</a>
                        </li>
                    </ul>
                </nav>
            </Suspense>
        </div>
    );
};

export default TodoDashboard;
