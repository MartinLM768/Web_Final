// Lambda function to handle customer comments
let comments = []; // Almacén temporal en memoria

exports.handler = async (event) => {
    try {
        const { httpMethod, body } = event;

        if (httpMethod === 'POST') {
            const { name, comment } = JSON.parse(body);

            if (!name || !comment) {
                return {
                    statusCode: 400,
                    body: JSON.stringify({ message: 'Name and comment are required.' }),
                };
            }

            const newComment = {
                id: comments.length + 1,
                name,
                comment,
                createdAt: new Date().toISOString(),
            };

            comments.push(newComment);

            return {
                statusCode: 201,
                body: JSON.stringify({ message: 'Comment saved successfully.', comment: newComment }),
            };
        }

        if (httpMethod === 'GET') {
            return {
                statusCode: 200,
                body: JSON.stringify(comments),
            };
        }

        return {
            statusCode: 405,
            body: JSON.stringify({ message: 'Method not allowed.' }),
        };
    } catch (error) {
        console.error(error);
        return {
            statusCode: 500,
            body: JSON.stringify({ message: 'An error occurred.' }),
        };
    }
};