$(sed 's/^/    /' << 'AUTOSCRIPT'
#!/bin/bash
# [Embed the same script content as above, indented for EOF]
# (For brevity, assume the prior script is placed here.)
echo "Running automated merge and cleanup..."
# ... (script contents from above) ...
echo "Automation script completed."
AUTOSCRIPT
)
