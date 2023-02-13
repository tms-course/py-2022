import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { FaTrash } from 'react-icons/fa';

import styles from './TodoItem.module.scss';

const TodoItem = ({ todo, updateTodo, deleteTodo }) => {
    const [editing, setEditing] = useState(false);
    const [desc, setDesc] = useState(todo.desc);
    const [done, setDone] = useState(todo.done);

    const handleEditing = () => {
        setEditing(true);
    };

    const handleUpdatedDesc = (event) => {
        if (event.key === 'Enter') {
            setEditing(false);
            updateTodo({...todo, desc });
        }
    };

    const handleComplete = () => {
        const newDone = !done;
        updateTodo({ ...todo, done: newDone });
        setDone(newDone);
    }

    return (
        <li className={styles.item}>
            { !editing ? (
                <div onDoubleClick={handleEditing}>
                    <input
                        type="checkbox"
                        className={styles.checkbox}
                        checked={done}
                        onChange={handleComplete}
                    />
                    <button type="button" onClick={() => deleteTodo(todo.id)}>
                        <FaTrash style={{ color: 'orangered', fontSize: '16px' }} />
                    </button>
                    <span className={done ? styles.complete : null}>{desc}</span>
                </div>
            ) : (
                <input
                    type="text"
                    className={styles.textInput}
                    value={desc}
                    onChange={(e) => setDesc(e.target.value)}
                    onKeyDown={handleUpdatedDesc}
                />
            )}
        </li>
    );
};

TodoItem.propTypes = {
    todo: PropTypes.isRequired,
};

TodoItem.propTypes = {
    updateTodo: PropTypes.func.isRequired,
    deleteTodo: PropTypes.func.isRequired,
};

export default TodoItem;
