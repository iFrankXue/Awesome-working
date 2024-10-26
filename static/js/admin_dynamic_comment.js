document.addEventListener('DOMContentLoaded', function () {
    const parentPostField = document.getElementById('id_parent_post');
    const parentCommentField = document.getElementById('id_parent_comment');

    if (parentPostField) {
        parentPostField.addEventListener('change', function () {
            const postId = this.value;
            if (postId) {
                // Make an AJAX request to fetch comments for the selected post
                fetch(`/admin/get-comments/?post_id=${postId}`)
                    .then(response => response.json())
                    .then(data => {
                        // Clear the existing options
                        parentCommentField.innerHTML = '<option value="">---------</option>';
                        // Populate the new options
                        data.comments.forEach(comment => {
                            const option = document.createElement('option');
                            option.value = comment.id;
                            option.textContent = comment.body;
                            parentCommentField.appendChild(option);
                        });
                    })
                    .catch(error => console.error('Error fetching comments:', error));
            } else {
                parentCommentField.innerHTML = '<option value="">---------</option>';
            }
        });
    }
});