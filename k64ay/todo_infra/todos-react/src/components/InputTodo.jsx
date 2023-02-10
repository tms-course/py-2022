import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { FaPlusCircle } from 'react-icons/fa';

const InputTodo = ({ addTodo }) => {
    const [inputText, setInputText] = useState('');

    const onChange = (e) => {
        setInputText(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (inputText.trim()) {
            addTodo(inputText);
            setInputText('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <input
                type="text"
                className="input-text"
                placeholder="Add todo..."
                value={inputText}
                onChange={onChange}
                name="desc"
            />
            <button type="button" className="input-submit">
                <FaPlusCircle
                    style={{ color: 'darkcyan', fontSize: '20px', marginTop: '2px' }}
                />
            </button>
        </form>
    );
};

InputTodo.propTypes = {
    addTodo: PropTypes.func.isRequired,
};

export default InputTodo;
