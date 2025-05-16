document.addEventListener('DOMContentLoaded', function() {
    // Copy to clipboard functionality
    document.querySelectorAll('.copy-btn').forEach(button => {
        button.addEventListener('click', function() {
            const textToCopy = this.getAttribute('data-clipboard-text');
            navigator.clipboard.writeText(textToCopy).then(() => {
                this.textContent = 'Copied!';
                setTimeout(() => {
                    this.textContent = 'Copy';
                }, 2000);
            });
        });
    });
    
    // Form validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const urlInput = this.querySelector('input[type="url"]');
            if (!urlInput.value) {
                e.preventDefault();
                urlInput.focus();
                alert('Please enter a URL');
            }
        });
    }
});
