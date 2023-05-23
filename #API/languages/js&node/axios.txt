Для отслеживания процесса загрузки используется:
  config: {
      onDownloadProgress: (progressEvent) => {
          progressEvent.lengthComputable // Возможно ли отслеживать прогресс

          let percentCompleted = Math.floor(
          (progressEvent.loaded / progressEvent.total) * 100
          );
          console.log("load: ", percentCompleted);
      }
  }
