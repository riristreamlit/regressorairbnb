1. Pastikan sudah install VSCode via Anaconda Navigator
2. Pastikan sudah download file file dari LMS
3. Buka VS Code, Open Folder >> Folder yang dipilih adalah folder hasil download dari LMS
4. Go to Terminal, New Terminal
5. Pastikan Terminal nya itu 'Command Prompt' dan bukan Powershell
6. Open Terminal, and type the following:
    - conda create -n streamlit-tutorial-env python=3.9 streamlit pandas numpy scikit-learn plotly matplotlib seaborn scipy jupyter ipykernel xgboost lightgbm networkx folium
    - conda activate streamlit-tutorial-env
    - pip install streamlit==1.24.0 streamlit-folium pipreqs
    - Kalo ada yang diminta 'y'/'n', atau 'yes'/'no', selalu isi dengan 'y' atau 'yes' 

7. Kalau mau nyobain streamlit, bisa run "streamlit run Hello.py", pastikan di Terminal itu ada di folder yang sama dengan file "Hello.py"
8. Kembali ke Terminal, pastikan:
    - Conda activate streamlit-tutorial-env
    - Pastikan teman-teman ada di dalam folder 'Steamlit Demo' (folder tempat kerja teman-teman, folder yang ada Hello.py nya)

9. Run this: pip list --format=freeze > pip_freeze.txt
10. Maka akan muncul pip_freeze.txt
11. Kembali ke Terminal, run: pipreqs
12. Maka akan muncul requirements.txt
13. Nah, di requirements.txt HASIL DARI PIPREQS, koreksi-lah versi dari masing-masing package, dengan melihat versi package tersebut di pip_freeze.txt

Jadi, pip_freeze.txt itu BENAR VERSI NYA, tapi banyak library yang ga penting dan ikut ditulis.
Tapi, requirements.txt itu BENAR LIST OF LIBRARIES NYA, tapi VERSI nya SALAH
Jadi file yang perlu diperbaiki adalah requirements.txt, dengan versi dari pip_freeze.txt

14. Upload seluruh folder dan seisinya ke github kalian
15. Buka share.streamlit.io, there you can deploy your app.


'Template' Folder Streamlit:
- Main App.py
- Exploration Notebook.ipynb
- Pages Folder:
    - Page 1
    - Page 2
    - dst
- Dataset Folder:
    - CSV
    - Dataset lain
- Model Folder:
    - Saved Machine Learning Model
- requirements.txt (streamit==1.24.0)