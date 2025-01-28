from typing import BinaryIO, Optional, Union
from uuid import uuid4

from sqlalchemy_file import File


def upload_file(
    file_content: Union[BinaryIO, bytes, str],
    filename: Optional[str] = None,
    content_type: Optional[str] = None,
) -> File:
    """
    Upload un fichier en utilisant sqlalchemy-file.
    
    Args:
        file_content: Le contenu du fichier (fichier ouvert, bytes ou string)
        filename: Nom du fichier (optionnel)
        content_type: Type MIME du fichier (optionnel)
        
    Returns:
        File: L'objet File créé
    """
    file = File(
        content=file_content,
        filename=filename,
        content_type=content_type,
        file_id=str(uuid4())
    )
    
    return file 